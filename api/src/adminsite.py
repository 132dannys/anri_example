from fastapi_amis_admin.admin.settings import Settings
from fastapi_amis_admin.admin.site import AdminSite
from fastapi_amis_admin.admin import admin
from fastapi_amis_admin.amis.components import PageSchema

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

# Create AdminSite instance
site = AdminSite(
    settings=Settings(database_url_async=f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"))


# Registration management class
@site.register_admin
class GitHubIframeAdmin(admin.IframeAdmin):
    # Set page menu information
    page_schema = PageSchema(label='AmisIframeAdmin', icon='fa fa-github')
    # Set the jump link
    src = 'https://github.com/amisadmin/fastapi_amis_admin'
