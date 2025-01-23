from . import models
from odoo.tools.safe_eval import safe_eval


def post_init_hook(env):
    """
    Post-init hook for the module.
    """

    try:
        # Récupère l'enregistrement 'max_users_limit' par son ID externe
        ref_record = env.ref("access_limit_max_users.max_users_limit")
    except ValueError as e:
        raise ValueError(
            "L'enregistrement 'max_users_limit' n'a pas été trouvé. "
            "Assurez-vous que l'ID externe est correct."
        ) from e

    # Vérifie que le domaine n'est pas vide
    if not ref_record.domain:
        ref_record.domain = "[]"  # Domaine par défaut si vide

    # Compte le nombre d'utilisateurs correspondant au domaine
    user_count = env["res.users"].search_count(safe_eval(ref_record.domain))

    # Met à jour le champ `max_records`
    ref_record.max_records = user_count
