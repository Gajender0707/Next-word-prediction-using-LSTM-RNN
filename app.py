import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle

st.title("Next Word Prediction ")
new_input_sent=st.text_input("Enter your Text")

#load the keras model
model=load_model("model.h5")

#load the pre-fit tokenizer
with open("tokenizer.pkl","rb") as f:
    tokenizer=pickle.load(f)

def next_word_prediction(new_sentence,model,tokenizer,max_length):
  print(new_sentence)
  tokenized_sentence=tokenizer.texts_to_sequences([new_sentence])
  sequenced_new_sent=pad_sequences(tokenized_sentence,maxlen=max_length,padding="pre")
  predicted_probabilities_values=model.predict(sequenced_new_sent)
  predicted_index = np.argmax(predicted_probabilities_values, axis=-1)[0]
  print(predicted_index)
  for value,index in tokenizer.word_index.items():
    if index==predicted_index:
      next_word=value

#   print(next_word)
  complete_sent=new_sentence+" "+ next_word
  return complete_sent

complete_sent=next_word_prediction(new_input_sent,model,tokenizer,14)


if st.button("Predict"):
    complete_sent