from src.LangGraphAgenticAI.ui.streamlitui.loadui import LoadStreamlitUI
from src.LangGraphAgenticAI.ui.streamlitui.display_result import DisplayResultStreamlit


def run_app() -> None:
    ui_loader = LoadStreamlitUI()
    user_controls = ui_loader.load_streamlit_ui()

    display = DisplayResultStreamlit(user_controls)
    display.render()
