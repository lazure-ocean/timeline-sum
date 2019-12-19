# Abstractive Timeline Summarization

Based on https://www.aclweb.org/anthology/D19-5403.pdf

## Architecture

1. clustering:
	* embeds using NSP
	* affinity propagation using TF-IDF cosine similarity
	* methods to synchronise dates
2. sentence generation:
	*  low-cost  MSC-system  by  Filippova(2010)
	* cluster = {date, sentence} -> sentence
	* in Russian here would be trubles: pymorphy, lemmatization, 
3. sentence scoring and selection
	* 3 steps
4. evaluation

### Additional: 
* seq2seq to make sentences grammatical
* Next sentence prediction
* natasha/razdel to split into sentences
* IlyaGusev/rnnmorph or pymorphy to split sentences into POS

## Useful links
https://github.com/natasha/natasha/tree/master/natasha
https://github.com/IlyaGusev/purano
