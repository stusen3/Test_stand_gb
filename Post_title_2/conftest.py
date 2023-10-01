import pytest


@pytest.fixture
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture
def btn_selector():
    return """//*[@id="login"]/div[3]/button"""


@pytest.fixture
def btn_add_selector():
    return """//*[@id="create-btn"]"""


@pytest.fixture
def title_input_selector():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture
def btn_save_selector():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture
def post_title_selector():
    return """//*[@id="app"]/main/div/div[1]/h1"""