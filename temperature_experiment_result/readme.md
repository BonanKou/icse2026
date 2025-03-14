This folder contains the post retrieved for 10 APIs by four baselines as well as our labels.
The format of the `retrieval_experiment.json` is:


```json
[
  {
    "name": "API_NAME",
    "language": "LANGUAGE",
    "popularity": "POPULARITY",
    "label_result": {
      "KNOWLEDGE_TYPE": {
        "finetuned_dpr": "ACCURACY",
        "dpr": "ACCURACY",
        "e5": "ACCURACY",
        "bm25": "ACCURACY"
      }
    },
    "retrieve_result": {
      "KNOWLEDGE_TYPE": {
        "finetuned_dpr": "POSTS",
        "dpr": "POSTS",
        "e5": "POSTS",
        "bm25": "POSTS"
      }
    }
  }
]
```

