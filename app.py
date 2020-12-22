"""A basic (single function) API written using Hug"""
from io import StringIO
import sys
import hug
import gitfame
import io
from git import Repo
import shutil
import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))


@hug.get('/exec_fame', output=hug.output_format.html, examples="url=https://github.com/diverso-lab/core.git")
def exec_fame(url: hug.types.text):
    if not url.startswith("https://github.com"):
        return "This is not supported"
    else:
        if not url.endswith(".git"):
            url=url+".git"
        _id=id_generator()
        Repo.clone_from(url, "./"+_id) 
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        gitfame.main(['--sort=commits', '-wt', './'+_id])
            
        sys.stdout = old_stdout
        try:
            shutil.rmtree("./"+_id)
        except OSError as e:
            print("Error: %s : %s" % ("./"+_id, e.strerror))
        return mystdout.getvalue().replace("\n","<br>")