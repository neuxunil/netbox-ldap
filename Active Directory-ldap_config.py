$ sudo nano /opt/netbox/netbox/netbox/ldap_config.py

import ldap
from django_auth_ldap.config import LDAPSearch, NestedGroupOfNamesType


AUTH_LDAP_SERVER_URI = "ldap://172.16.0.2"

AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_REFERRALS: 0
}

AUTH_LDAP_BIND_DN = "cn=netbox_s,ou=ServiceAccounts,ou=MSK,dc=itdraft,dc=ru"
AUTH_LDAP_BIND_PASSWORD = "3ghJnd56hff"

LDAP_IGNORE_CERT_ERRORS = True

AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=Users,ou=MSK,dc=itdraft,dc=ru", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")

AUTH_LDAP_USER_DN_TEMPLATE = None

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Groups,ou=MSK,dc=itdraft,dc=ru", ldap.SCOPE_SUBTREE, "(objectClass=group)")

AUTH_LDAP_GROUP_TYPE = NestedGroupOfNamesType(name_attr="cn")


AUTH_LDAP_ALWAYS_UPDATE_USER = True

#AUTH_LDAP_MIRROR_GROUPS = True

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=00.gruop.001,ou=Groups,ou=MSK,dc=itdraft,dc=ru",
    "is_staff": "cn=00.gruop.001,ou=Groups,ou=MSK,dc=itdraft,dc=ru",
    "is_superuser": "cn=00.gruop.001,ou=Groups,ou=MSK,dc=itdraft,dc=ru"
}

AUTH_LDAP_FIND_GROUP_PERMS = True

AUTH_LDAP_CACHE_TIMEOUT = 3600

AUTHENTICATION_BACKENDS = (
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
)

