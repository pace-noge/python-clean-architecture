import pytest

from manage import read_json_configuration
from application.app import create_app


@pytest.fixture()
def app():
    app = create_app("testing")
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def pytest_adoption(parser):
    parser.adoption(
        "--integration", action="store_true", help="run integration tests"
    )


def pytest_runtest_setup(item):
    if "integration" in item.keywords and not item.config.getvalue(
        "integration"
    ):
        pytest.skip("need --integration option to run")


@pytest.fixture(scope="session")
def app_configuration():
    return read_json_configuration("testing")