import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

from app import app

def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=4)
    header = dash_duo.find_element("#header")
    assert header is not None

def test_visualization_is_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#visualization", timeout=4)
    graph = dash_duo.find_element("#visualization")
    assert graph is not None

def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-picker", timeout=4)
    picker = dash_duo.find_element("#region-picker")
    assert picker is not None