"""The Accounts security log."""

from pages.accounts.admin.base import AccountsAdmin


class Doorkeeper(AccountsAdmin):
    """The OAuth application list."""

    URL_TEMPLATE = '/oauth/applications'


class Security(AccountsAdmin):
    """The Accounts security log entries page."""

    URL_TEMPLATE = '/security_log{query_string}'
