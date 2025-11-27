import pytest
from core.base_ui import BaseUI

@pytest.fixture
def browser():
    ui = BaseUI()
    driver = ui.setup_browser()
    yield driver
    ui.teardown_browser()