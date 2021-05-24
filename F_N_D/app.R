library(shiny)
library(tidyverse)
library(tm)
library(qdapRegex)
library(keras)
library(wordcloud)
library(shinythemes)
library(plotly)

# Define UI for application that draws a histogram
ui <- fluidPage(
    theme = shinytheme("cyborg"),
    img(src = "image.jpg", height = 250, width = "100%"),
    # Application title
    titlePanel("Fake News Detection"),

    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
            textInput("title", "Title", placeholder = "Enter the News Title here"),
            textInput("Content", "News Content", placeholder = "Enter the News Content here"),
            submitButton(text = "Check", width = "100%")
        ),
        # Show a plot of the generated distribution
        mainPanel(
            tabsetPanel(
                tabPanel("Result", HTML(
                    '<p><strong>News Title</strong><br></p>'
                ),
                         textOutput("title_print"),
                HTML(
                    '<p><br><br><strong>News Content</strong></p>'
                ),
                        textOutput("News_content"),
                HTML(
                    '<p><br><br><strong>Final Verdict</strong></p>'
                ),
                        textOutput("Final_verdict"),
                HTML(
                    '<p><br><br><strong>Percentage</strong></p>'
                ),
                        textOutput("Percentage")),
                tabPanel("Plot",
                         HTML(
                             '<p>Below is the Wordcloud of the Input sequence<br><br></p>'
                         ),
                         plotOutput("WordCloud"),
                         HTML(
                             '<p>Below is theMost repeated word in the news<br><br></p>'
                         ),
                         plotlyOutput("Geom_bar")),
                tabPanel("Info",
                         HTML(
                             '<p>This project is made using BiLSTM gate and made the full capacity of the model to predict
the News on the Unknown sample.<br>This project is made using keras and created the shiny UI for demonstration purpose.</p>'
                         )),
                tabPanel("Disclaimer", HTML(
                    '<p><li> This project is intended to showcase the fake news capability of the deep learning model using LSTM Gate</li>
                    <li> We do not accept any liability if this project is used for an alternative purpose from which it is intended, nor to any third party in respect of this project
                    </li></p>'
                )),
                tabPanel("Change Theme",shinythemes::themeSelector())
            )
        )
    )
)

server <- function(input, output) {
    output$title_print <- renderText({input$title})
    output$News_content <- renderText({input$Content})
    output$Final_verdict <- renderText({ifelse(Analyse(input$title, input$Content, 0) == 0, "TRUE", "FALSE")})
    output$Percentage <- renderText({Analyse(input$title, input$Content, 1)})
    output$WordCloud <- renderPlot({Plot_Wordcloud(input$title, input$Content, 0)})
    output$Geom_bar <- renderPlotly({Plot_Wordcloud(input$title, input$Content, 1)})
}

Analyse <- function(title, content, percentage = 0){
    news <- paste0(title, " ", content)
    stopwords <- stopwords::stopwords(language = "en")
    news = gsub("[^A-Za-z]", " ", news)
    news = stripWhitespace(news)
    news = removeWords(news, stopwords)
    news = stripWhitespace(news)
    news = removePunctuation(news)
    news = stripWhitespace(news)
    news = stemDocument(news)
    news = stripWhitespace(news)
    news = rm_nchar_words(news, "1,3")
    news = stripWhitespace(news)
    news = tolower(news)
    
    voc_size = 30000
    
    tokenise = text_tokenizer(num_words = voc_size) %>%
        fit_text_tokenizer(news)
    
    sequences = texts_to_sequences(tokenise, news)
    
    
    sent_length = 100
    embedded_sample = pad_sequences(sequences, maxlen=sent_length)
    
    model = load_model_hdf5("./model_1/1M_85P_ACC.h5")
    prediction = 0
    if(percentage == 0){
        prediction = model %>% predict_classes(embedded_sample)
        
    } else {
        prediction = model %>% predict(embedded_sample)
        prediction = round(100 - (prediction * 100), 2)
    }
    prediction
}

Plot_Wordcloud <- function(title, Content, operation = 0){
    string = paste0(title, " ", Content)
    string = gsub("[^A-Za-z]"," ", string)
    corpus <- VCorpus(VectorSource(string))
    corpus <- tm_map(corpus,content_transformer(tolower))
    corpus <- tm_map(corpus,removeNumbers)
    corpus <- tm_map(corpus,removePunctuation)
    corpus <- tm_map(corpus,removeWords, stopwords())
    corpus <- tm_map(corpus, stemDocument)
    corpus <- tm_map(corpus, stripWhitespace)
    
    dtm = TermDocumentMatrix(corpus)
    matrix = as.matrix(dtm) 
    words = sort(rowSums(matrix),decreasing=TRUE) 
    df = data.frame(word = names(words),freq=words)
    if(operation == 0){
        figure = wordcloud(words = df$word, freq = df$freq, 
                           min.freq = 1, max.words = 20, random.order = F, scale = c(4,1),
                           rot.per = 0.3, colors = brewer.pal(8, "Accent"))
    } else if(operation == 1){
        df = df[1:20,]
        figure = ggplotly(ggplot(df, aes(freq, reorder(word, freq), fill = word)) + 
                              geom_bar(stat = "identity") + labs(x = "Frequency of the words", y = "Repeated words",
                                                                 title = "Top 20 Most Repeated Words in the Data") + 
                              theme(legend.position = "none"))
    }
    figure
}



# Run the application 
shinyApp(ui = ui, server = server)
