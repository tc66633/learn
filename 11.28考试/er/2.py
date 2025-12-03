from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

file_path = "D:/learn/11.28考试/er/corpus.txt"

with open(file_path, "r", encoding="utf-8") as file:
    corpus_text = file.read()

corpus_text = corpus_text.replace("\n", " <eos> ")
corpus_tokens = corpus_text.split()

def create_sequence_prediction_data(text, window_size=3):
    inputs = []
    outputs = []
    for i in range(len(text) - window_size):
        inputs.append(text[i:i+window_size])
        outputs.append(text[i+window_size])
    return inputs, outputs

window_size = 3
inputs, outputs = create_sequence_prediction_data(corpus_tokens, window_size)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(inputs + outputs)

X = tokenizer.texts_to_sequences(inputs)
y = tokenizer.texts_to_sequences(outputs)

max_sequence_length = 5
X_pad = pad_sequences(X, maxlen=max_sequence_length, padding='pre')
y_pad = pad_sequences(y, maxlen=1, padding='pre')

# 构建模型
vocab_size = len(tokenizer.word_index) + 1
embedding_dim = 100

model = Sequential([
    Embedding(vocab_size, embedding_dim, input_length=max_sequence_length),
    LSTM(128, return_sequences=False),
    Dropout(0.2),
    Dense(vocab_size, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.summary()

model.fit(X_pad, np.array(y_pad), epochs=50, batch_size=32)  # 可以增加训练轮次

inputs, outputs = create_sequence_prediction_data(corpus_text, window_size=5)  # 调整窗口大小

def generate_text(model, tokenizer, input_text, max_sequence_length=5, temperature=1.0):
    sequence = tokenizer.texts_to_sequences([input_text.split()])
    sequence_pad = pad_sequences(sequence, maxlen=max_sequence_length, padding='pre')

    predicted_probabilities = model.predict(sequence_pad)

    predicted_probabilities = predicted_probabilities / temperature
    predicted_probabilities = np.exp(predicted_probabilities) / np.sum(np.exp(predicted_probabilities), axis=-1,
                                                                       keepdims=True)

    predicted_index = np.argmax(predicted_probabilities, axis=-1)

    predicted_word = tokenizer.index_word[predicted_index[0]]
    return predicted_word


input_prefix = "我 喜欢 深度"
predicted_word = generate_text(model, tokenizer, input_prefix, temperature=0.7)
print(f"输入: {input_prefix}，预测下一个词: {predicted_word}")

