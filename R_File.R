library(tidyverse)
library(tm)
library(qdapRegex)
library(keras)
library(caret)

train_data <- read.csv("./Data/train.csv") %>% drop_na()
test_data <- read.csv("./Data/test.csv") %>% drop_na()
submit_data <- read.csv("./Data/submit.csv") %>% drop_na()


test_data$label <- submit_data$label

final_data <- rbind(train_data, test_data)
final_data$cleaned_data <- paste0(final_data$title, " ", final_data$text)
stop_words <- stopwords::stopwords(language = "en")

for(i in 1:nrow(final_data)){
  final_data$cleaned_data[i] = gsub("[^A-Za-z]", " ", final_data$cleaned_data[i])
  final_data$cleaned_data[i] = stripWhitespace(final_data$cleaned_data[i])
  final_data$cleaned_data[i] = removeWords(final_data$cleaned_data[i], stop_words)
  final_data$cleaned_data[i] = stripWhitespace(final_data$cleaned_data[i])
  final_data$cleaned_data[i] = removePunctuation(final_data$cleaned_data[i])
  final_data$cleaned_data[i] = stripWhitespace(final_data$cleaned_data[i])
  final_data$cleaned_data[i] = stemDocument(final_data$cleaned_data[i])
  final_data$cleaned_data[i] = stripWhitespace(final_data$cleaned_data[i])
  final_data$cleaned_data[i] = rm_nchar_words(final_data$cleaned_data[i], "1,3")
  final_data$cleaned_data[i] = stripWhitespace(final_data$cleaned_data[i])
  final_data$cleaned_data[i] = tolower(final_data$cleaned_data[i])
}


voc_size = 30000#length(unique(unlist(str_split(final_data$cleaned_data[1:nrow(final_data)],pattern = " "))))


tokenizer_testing <- text_tokenizer(num_words = voc_size) %>%
  fit_text_tokenizer(final_data$cleaned_data)

sequences_testing <- texts_to_sequences(tokenizer_testing, final_data$cleaned_data)


sent_length = 100
embedded_docs_testing = pad_sequences(sequences_testing, maxlen=sent_length)
embedding_vector_features = 32

samples <- sample(1:nrow(final_data), size = 0.8*nrow(final_data))
x_train = embedded_docs_testing[samples,]
y_train = final_data$label[samples]

x_test = embedded_docs_testing[-samples,]
y_test = final_data$label[-samples]


model <- keras_model_sequential() %>%
  layer_embedding(input_dim = voc_size, input_length = sent_length, output_dim = embedding_vector_features) %>%
  bidirectional(layer_lstm(units = 32, activation = "softmax", recurrent_dropout = 0.1)) %>%
  layer_dense(units = 1, activation = "sigmoid") %>%
  compile(
    optimizer = "adam",
    loss = "binary_crossentropy",
    metrics = c("acc")
  )

history <- model %>% fit(
  x_train, y_train,
  epochs = 5, batch_size = 128, validation_split = 0.1
)


prediction <- model %>%
  predict_classes(x_test)

confusionMatrix(factor(prediction), factor(y_test))


save_model_hdf5(model, filepath = "./model/model_1/1M_85P_ACC.h5")
save_model_weights_hdf5(model, filepath = "./model/model_1/1M_85P_ACC_WEIGHTS.h5")






