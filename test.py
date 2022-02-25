import pickle


with open('export.pkl', 'rb') as f:
    data = pickle.load(f)
    res = data.predict('bear.jpg')
    print(res)

