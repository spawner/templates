# for making the web app
library(shiny)
# for accessing webpages
library(httr)
# for handling strings
library(stringr)
# for handling json
library(jsonlite)
# for plotting
library(ggplot2)
# for prettier plots
library(ggthemes)
# for themes
library(shinythemes)


###
# Sets up the UI with a shinytheme, two text input boxes in the sidebar that take in
# an API key and a question, and passes that input to the server script, which returns
# a plot of closing price data on the 'Plot' tab and the table of financial data on
# the 'Table' tab.
###
ui = fluidPage(theme = shinytheme("flatly"),
  titlePanel("Spawner.AI /answer R+Shiny Demo"),
  
  sidebarLayout(
    sidebarPanel(
      helpText("Ask a question about financial data"),
      
      textInput("api_key", "Input Your API Key", "Your api key here"),
      textInput("question", "Ask Your Question", "What is the stock price of aapl"),
      
    ),
    
    mainPanel(
      tabsetPanel(
        tabPanel("Plot", plotOutput("plot")),
        tabPanel("Table", tableOutput("table"))
      )
    )
  )
)


###
# Takes in the API key and question and uses the API to get the data as a 
# JSON object. It then builds a plot of closing prices and table of the data
# which are rendered in the UI.
###
server <- function(input, output) {
  
  dataInput <- reactive({
    
    as.data.frame(fromJSON(paste("https://spawnerapi.com/answer", 
                                 str_replace_all(input$question, 
                                                 pattern=" ", 
                                                 replacement="%20"), 
                                 input$api_key, # api key
                                 sep = "/", 
                                 collapse = NULL))$data)
  })
  
  
  output$plot <- renderPlot({
    data <- dataInput()
    
    ggplot(data = data,
           aes(x=date, y=close, group = 1)) + 
      geom_line(color="red",
                size=1) +
      theme_fivethirtyeight() +
      theme(axis.text.x=element_text(angle=60, hjust=1)) +
      ggtitle(input$question)
  })
  
  output$table <- renderTable({
    data <- dataInput()
  })
  
}

# Runs the app
shinyApp(ui = ui, server = server)