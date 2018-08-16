# coding: utf-8

from the import expect

from filesystem import Paths
from filesystem.Paths import Root


class TestFilesystemPaths:

    def setup_method(self):
        pass

    def test_that_root_exists(self):
        expect(Paths.ROOT).to.be.NOT.empty

    def test_that_app_is_correct(self):
        expect(Paths.APP).to.be.eq('/app')

    def test_that_app_http_is_correct(self):
        expect(Paths.APP_HTTP).to.be.eq('/app/http')

    def test_that_app_http_controllers_is_correct(self):
        expect(Paths.APP_HTTP_CONTROLLERS).to.be.eq('/app/http/controllers')

    def test_that_app_http_middleware_is_correct(self):
        expect(Paths.APP_HTTP_MIDDLEWARE).to.be.eq('/app/http/middleware')

    def test_that_app_providers_is_correct(self):
        expect(Paths.APP_PROVIDERS).to.be.eq('/app/providers')

    def test_that_bootstrap_is_correct(self):
        expect(Paths.BOOTSTRAP).to.be.eq('/bootstrap')

    def test_that_bootstrap_cache_is_correct(self):
        expect(Paths.BOOTSTRAP_CACHE).to.be.eq('/bootstrap/cache')

    def test_that_config_is_correct(self):
        expect(Paths.CONFIG).to.be.eq('/config')

    def test_that_databases_is_correct(self):
        expect(Paths.DATABASES).to.be.eq('/databases')

    def test_that_databases_migrations_is_correct(self):
        expect(Paths.DATABASES_MIGRATIONS).to.be.eq('/databases/migrations')

    def test_that_resources_is_correct(self):
        expect(Paths.RESOURCES).to.be.eq('/resources')

    def test_that_resources_templates_is_correct(self):
        expect(Paths.RESOURCES_TEMPLATES).to.be.eq('/resources/templates')

    def test_that_routes_is_correct(self):
        expect(Paths.ROUTES).to.be.eq('/routes')

    def test_that_storage_is_correct(self):
        expect(Paths.STORAGE).to.be.eq('/storage')

    def test_that_storage_compiled_is_correct(self):
        expect(Paths.STORAGE_COMPILED).to.be.eq('/storage/compiled')

    def test_that_storage_static_is_correct(self):
        expect(Paths.STORAGE_STATIC).to.be.eq('/storage/static')

    def test_that_storage_uploads_is_correct(self):
        expect(Paths.STORAGE_UPLOADS).to.be.eq('/storage/uploads')

    def test_that_tests_is_correct(self):
        expect(Paths.TESTS).to.be.eq('/tests')

    # Root Paths

    def test_that_root_app_is_correct(self):
        expect(Root.APP).to.be.eq(Paths.ROOT + Paths.APP)

    def test_that_root_app_http_is_correct(self):
        expect(Root.APP_HTTP).to.be.eq(Paths.ROOT + Paths.APP_HTTP)

    def test_that_root_app_http_controllers_is_correct(self):
        expect(Root.APP_HTTP_CONTROLLERS).to.be.eq(Paths.ROOT + Paths.APP_HTTP_CONTROLLERS)

    def test_that_root_app_http_middleware_is_correct(self):
        expect(Root.APP_HTTP_MIDDLEWARE).to.be.eq(Paths.ROOT + Paths.APP_HTTP_MIDDLEWARE)

    def test_that_root_app_providers_is_correct(self):
        expect(Root.APP_PROVIDERS).to.be.eq(Paths.ROOT + Paths.APP_PROVIDERS)

    def test_that_root_bootstrap_is_correct(self):
        expect(Root.BOOTSTRAP).to.be.eq(Paths.ROOT + Paths.BOOTSTRAP)

    def test_that_root_bootstrap_cache_is_correct(self):
        expect(Root.BOOTSTRAP_CACHE).to.be.eq(Paths.ROOT + Paths.BOOTSTRAP_CACHE)

    def test_that_root_config_is_correct(self):
        expect(Root.CONFIG).to.be.eq(Paths.ROOT + Paths.CONFIG)

    def test_that_root_databases_is_correct(self):
        expect(Root.DATABASES).to.be.eq(Paths.ROOT + Paths.DATABASES)

    def test_that_root_databases_migrations_is_correct(self):
        expect(Root.DATABASES_MIGRATIONS).to.be.eq(Paths.ROOT + Paths.DATABASES_MIGRATIONS)

    def test_that_root_resources_is_correct(self):
        expect(Root.RESOURCES).to.be.eq(Paths.ROOT + Paths.RESOURCES)

    def test_that_root_resources_templates_is_correct(self):
        expect(Root.RESOURCES_TEMPLATES).to.be.eq(Paths.ROOT + Paths.RESOURCES_TEMPLATES)

    def test_that_root_routes_is_correct(self):
        expect(Root.ROUTES).to.be.eq(Paths.ROOT + Paths.ROUTES)

    def test_that_root_storage_is_correct(self):
        expect(Root.STORAGE).to.be.eq(Paths.ROOT + Paths.STORAGE)

    def test_that_root_storage_compiled_is_correct(self):
        expect(Root.STORAGE_COMPILED).to.be.eq(Paths.ROOT + Paths.STORAGE_COMPILED)

    def test_that_root_storage_static_is_correct(self):
        expect(Root.STORAGE_STATIC).to.be.eq(Paths.ROOT + Paths.STORAGE_STATIC)

    def test_that_root_storage_uploads_is_correct(self):
        expect(Root.STORAGE_UPLOADS).to.be.eq(Paths.ROOT + Paths.STORAGE_UPLOADS)

    def test_that_root_tests_is_correct(self):
        expect(Root.TESTS).to.be.eq(Paths.ROOT + Paths.TESTS)
