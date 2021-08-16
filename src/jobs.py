from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents
    q
        Parameters
        ----------
        path : str
            Full path to file

        Returns
        -------
        list
            List of rows as dicts
    """
    with open(path) as jobs_file:
        data = csv.DictReader(jobs_file, delimiter=",", quotechar='"')
        content = list(data)
        return content


print(read("./src/jobs.csv"))
