from sklearn.feature_extraction.text import TfidfVectorizer

poems = [['कौन-सी','राह','है','वो','आधुनिक','काल','है'],
		['कौन-सी','राह','वो','आधुनिक','का'],
		['कौन-सी','राह','है','व','आधुन','काल']]

def identity_func(doc):
	return doc

btf = TfidfVectorizer(binary=True,
	norm=None,
	use_idf=False,
	smooth_idf=False,
	lowercase=False,
	tokenizer=identity_func,
	preprocessor=identity_func,
	max_df = 0.8,
	token_pattern=None)

btf.fit(poems)
print(btf.vocabulary_)
print(btf.transform(poems).toarray())

bow = TfidfVectorizer(binary=False,
	norm=None,
	use_idf=False,
	smooth_idf=False,
	lowercase=False,
	tokenizer=identity_func,
	preprocessor=identity_func,
	max_df = 0.8,
	token_pattern=None)

bow.fit(poems)
print(bow.transform(poems).toarray())
# print(bow.transform([poems[0]]).toarray()[0])


tfl1 = TfidfVectorizer(binary=False,
	norm='l1',
	use_idf=False,
	smooth_idf=False,
	lowercase=False,
	tokenizer=identity_func,
	preprocessor=identity_func,
	max_df = 0.8,
	token_pattern=None)

tfl1.fit(poems)
print(tfl1.transform(poems).toarray())

tfidf = TfidfVectorizer(binary=False,
	norm='l2',
	use_idf=True,
	smooth_idf=True,
	lowercase=False,
	tokenizer=identity_func,
	preprocessor=identity_func,
	max_df = 0.8,
	token_pattern=None)

tfidf.fit(poems)
print(tfidf.transform(poems).toarray())