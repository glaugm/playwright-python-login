from playwright.sync_api import Page, expect

def test_login_senha_incorreta(page:Page):
    page.goto("https://gotasdetecnologia.com.br/testes-curso01/login-js/index.html")

    page.get_by_role("textbox", name="Email").fill("teste@teste.com")
    page.get_by_role("textbox", name="Senha").fill("123456")

    page.get_by_role("button", name="Entrar").click()

    expect(page.get_by_text("Tentativa 1 de 3. Senha incorreta.", exact=True)).to_be_visible() #assertion


def test_login_sucesso(page:Page):
    page.goto("https://gotasdetecnologia.com.br/testes-curso01/login-js/index.html")

    page.get_by_role("textbox", name="Email").fill("qa.playwright.teste@gmail.com")
    page.get_by_role("textbox", name="Senha").fill("Play@1234")

    page.get_by_role("button", name="Entrar").click()

    expect(page).to_have_url(
        "https://gotasdetecnologia.com.br/testes-curso01/login-js/dashboard.html"
        ) 
    expect(page.get_by_text("Bem-vindo, QA Playwright!")).to_be_visible() 