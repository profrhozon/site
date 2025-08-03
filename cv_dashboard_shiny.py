from shiny import App, ui

# Definindo a interface com abas (dashboard)
app_ui = ui.page_fluid(
    ui.h1("Meu Currículo Digital - Dashboard"),
    ui.navset_tab(
         ui.nav("Dados Pessoais", 
             ui.row(
                 ui.column(12, 
                     ui.p("Nome: Fulano de Tal"),
                     ui.p("Email: fulano@example.com"),
                     ui.p("Telefone: (00) 1234-5678")
                 )
             )
         ),
         ui.nav("Experiência Profissional", 
             ui.row(
                 ui.column(12, 
                     ui.ul(
                         ui.li("Empresa X - Cargo Y (Ano de início - Ano de término)"),
                         ui.li("Empresa Z - Cargo W (Ano de início - Ano de término)")
                     )
                 )
             )
         ),
         ui.nav("Educação",
             ui.row(
                 ui.column(12,
                     ui.p("Graduação em Exemplo, Universidade ABC (Ano de conclusão)")
                 )
             )
         ),
         ui.nav("Habilidades",
             ui.row(
                 ui.column(12,
                     ui.ul(
                         ui.li("Python"),
                         ui.li("Streamlit"),
                         ui.li("Shiny for Python"),
                         ui.li("Outras habilidades relevantes")
                     )
                 )
             )
         )
    )
)

# Criação do aplicativo sem lógica reativa adicional
app = App(app_ui, None)

if __name__ == '__main__':
    app.run()
