# coding: utf-8

from the import expect

from filesystem import paths
from filesystem.paths import root


class TestFilesystemPaths:

    def setup_method(self):
        pass

    def test_that_root_exists(self):
        expect(paths.ROOT).to.be.NOT.empty

    def test_that_app_is_correct(self):
        expect(paths.APP).to.be.eq('/app')

    def test_that_app_http_is_correct(self):
        expect(paths.APP_HTTP).to.be.eq('/app/http')

    def test_that_app_http_controllers_is_correct(self):
        expect(paths.APP_HTTP_CONTROLLERS).to.be.eq('/app/http/controllers')

    def test_that_app_http_middleware_is_correct(self):
        expect(paths.APP_HTTP_MIDDLEWARE).to.be.eq('/app/http/middleware')

    def test_that_app_providers_is_correct(self):
        expect(paths.APP_PROVIDERS).to.be.eq('/app/providers')

    def test_that_bootstrap_is_correct(self):
        expect(paths.BOOTSTRAP).to.be.eq('/bootstrap')

    def test_that_bootstrap_cache_is_correct(self):
        expect(paths.BOOTSTRAP_CACHE).to.be.eq('/bootstrap/cache')

    def test_that_config_is_correct(self):
        expect(paths.CONFIG).to.be.eq('/config')

    def test_that_databases_is_correct(self):
        expect(paths.DATABASES).to.be.eq('/databases')

    def test_that_databases_migrations_is_correct(self):
        expect(paths.DATABASES_MIGRATIONS).to.be.eq('/databases/migrations')

    def test_that_resources_is_correct(self):
        expect(paths.RESOURCES).to.be.eq('/resources')

    def test_that_resources_templates_is_correct(self):
        expect(paths.RESOURCES_TEMPLATES).to.be.eq('/resources/templates')

    def test_that_resources_snippets_is_correct(self):
        expect(paths.RESOURCES_SNIPPETS).to.be.eq('/resources/snippets')

    def test_that_routes_is_correct(self):
        expect(paths.ROUTES).to.be.eq('/routes')

    def test_that_storage_is_correct(self):
        expect(paths.STORAGE).to.be.eq('/storage')

    def test_that_storage_compiled_is_correct(self):
        expect(paths.STORAGE_COMPILED).to.be.eq('/storage/compiled')

    def test_that_storage_static_is_correct(self):
        expect(paths.STORAGE_STATIC).to.be.eq('/storage/static')

    def test_that_storage_uploads_is_correct(self):
        expect(paths.STORAGE_UPLOADS).to.be.eq('/storage/uploads')

    def test_that_tests_is_correct(self):
        expect(paths.TESTS).to.be.eq('/tests')

    # root paths

    def test_that_root_app_is_correct(self):
        expect(root.APP).to.be.eq(paths.ROOT + paths.APP)

    def test_that_root_app_http_is_correct(self):
        expect(root.APP_HTTP).to.be.eq(paths.ROOT + paths.APP_HTTP)

    def test_that_root_app_http_controllers_is_correct(self):
        expect(root.APP_HTTP_CONTROLLERS).to.be.eq(paths.ROOT + paths.APP_HTTP_CONTROLLERS)

    def test_that_root_app_http_middleware_is_correct(self):
        expect(root.APP_HTTP_MIDDLEWARE).to.be.eq(paths.ROOT + paths.APP_HTTP_MIDDLEWARE)

    def test_that_root_app_providers_is_correct(self):
        expect(root.APP_PROVIDERS).to.be.eq(paths.ROOT + paths.APP_PROVIDERS)

    def test_that_root_bootstrap_is_correct(self):
        expect(root.BOOTSTRAP).to.be.eq(paths.ROOT + paths.BOOTSTRAP)

    def test_that_root_bootstrap_cache_is_correct(self):
        expect(root.BOOTSTRAP_CACHE).to.be.eq(paths.ROOT + paths.BOOTSTRAP_CACHE)

    def test_that_root_config_is_correct(self):
        expect(root.CONFIG).to.be.eq(paths.ROOT + paths.CONFIG)

    def test_that_root_databases_is_correct(self):
        expect(root.DATABASES).to.be.eq(paths.ROOT + paths.DATABASES)

    def test_that_root_databases_migrations_is_correct(self):
        expect(root.DATABASES_MIGRATIONS).to.be.eq(paths.ROOT + paths.DATABASES_MIGRATIONS)

    def test_that_root_resources_is_correct(self):
        expect(root.RESOURCES).to.be.eq(paths.ROOT + paths.RESOURCES)

    def test_that_root_resources_templates_is_correct(self):
        expect(root.RESOURCES_TEMPLATES).to.be.eq(paths.ROOT + paths.RESOURCES_TEMPLATES)

    def test_that_root_resources_snippets_is_correct(self):
        expect(root.RESOURCES_SNIPPETS).to.be.eq(paths.ROOT + paths.RESOURCES_SNIPPETS)

    def test_that_root_routes_is_correct(self):
        expect(root.ROUTES).to.be.eq(paths.ROOT + paths.ROUTES)

    def test_that_root_storage_is_correct(self):
        expect(root.STORAGE).to.be.eq(paths.ROOT + paths.STORAGE)

    def test_that_root_storage_compiled_is_correct(self):
        expect(root.STORAGE_COMPILED).to.be.eq(paths.ROOT + paths.STORAGE_COMPILED)

    def test_that_root_storage_static_is_correct(self):
        expect(root.STORAGE_STATIC).to.be.eq(paths.ROOT + paths.STORAGE_STATIC)

    def test_that_root_storage_uploads_is_correct(self):
        expect(root.STORAGE_UPLOADS).to.be.eq(paths.ROOT + paths.STORAGE_UPLOADS)

    def test_that_root_tests_is_correct(self):
        expect(root.TESTS).to.be.eq(paths.ROOT + paths.TESTS)
