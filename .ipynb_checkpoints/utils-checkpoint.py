import pandas as pd


def process_parser_data(file_name, start_date=None, end_date=None):
    dataset = pd.read_csv(
        file_name, sep=',', quotechar='\"', escapechar='\\',
        encoding='utf-8', error_bad_lines=False, header=0,
        verbose=False, keep_date_col=True, index_col=False)
    dataset = dataset[["date", "url", "edition", "title", "text", "authors", "topics"]]
    dataset = dataset[(~dataset["text"].isnull() & ~dataset["title"].isnull())]
    dataset["date"] = pd.to_datetime(dataset["date"])
    dataset["text"] = dataset["text"].apply(lambda x: x.replace("\\n", " "))
    dataset["edition"] = dataset["edition"].apply(lambda x: None if x == "-" else x)
    if start_date:
        dataset = dataset[dataset["date"] >= start_date]
    if end_date:
        dataset = dataset[dataset["date"] < end_date]
    dataset.sort_values("date", inplace=True)
    dataset.drop_duplicates(subset=["title", "text"], keep='last', inplace=True)
    dataset.drop_duplicates(subset=["url"], keep='last', inplace=True)
    print(dataset.info())
    print(dataset.head(5))
    return dataset
