from oauth2_provider.models import AbstractApplication

from authserver.metadata import MetaData


class OauthApplication(AbstractApplication,MetaData):

    class Meta:
        db_table="oauthapplication"
