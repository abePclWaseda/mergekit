import datasets
ds = datasets.load_dataset("metaeval/spartqa-mchoice")
slice_ds = ds["test"].select(range(200))
ds["test"] = slice_ds
slice_ds = ds["train"].select(range(200))
ds["train"] = slice_ds
ds.save_to_disk("./spartqa-mchoice-200")