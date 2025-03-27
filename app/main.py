from shiny import App, render, ui

# UI 정의
app_ui = ui.page_fluid(
    ui.h1("Restaurant Tip Analysis Dashboard")
)

# 서버 로직 정의
def server(input, output, session):
    pass

# 앱 생성
app = App(app_ui, server) 