# Abstractive Timeline Summarization

Based on https://www.aclweb.org/anthology/D19-5403.pdf

## Architecture
0. sentence embeddings
	* embed sentences using NSP
1. clustering
	* clustering maps `{collection of all sentences from all articles}` to `{collection of grouped sentences i.e. clusters}`
	* affinity propagation using TF-IDF cosine similarity
	* methods to synchronise dates
	* use from `purano`
2. dates extraction
	* dates extraction maps `{collection of clusters}` to `{collection of dates}`
	* for each sentence extract the date the event it refers to took place
3. sentence generation
	* sentence generation maps `{collection of pairs (cluster, date)}` to `{collection of sentences}`
	* low-cost  MSC-system  by  Filippova(2010)
	* in Russian here would be trubles: pymorphy, lemmatization, 
4. sentence scoring and selection
	* 3 steps
5. evaluation

### Additional
* seq2seq to make sentences grammatical
* Next sentence prediction
* natasha/razdel to split into sentences
* IlyaGusev/rnnmorph or pymorphy to split sentences into POS

## Useful links
* https://github.com/natasha/natasha/tree/master/natasha
* https://github.com/IlyaGusev/purano
* https://github.com/julmaxi/Abstractive-Timeline-Summarization
