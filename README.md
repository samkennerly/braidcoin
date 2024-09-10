# Braidcoin

Experiments in a improving Bitcoin using a Directed Acyclic Graph


## run with Docker

If you have [Docker desktop] installed, `cd` to this repo and run
```
./serve
```
then point a web browser here:
```
127.0.0.1:8888
```
Docker will [bind mount] folders from this repo and create an `etc/` folder for Jupyter config files. The container will not have permission to modify files outside this repo.

[Docker desktop]: https://www.docker.com/products/docker-desktop/
[bind mount]: https://docs.docker.com/engine/storage/bind-mounts/


## run without Docker

Running these examples requires [Jupyter] and the ipython kernel.  Fire up the example notebook in your browser by `jupyter notebook`.

We use [graph_tool] for plotting. This one is a bitch to compile, I recommend getting it from your friendly local pre-compiled distribution. I use Ubuntu 16.04.  The dependencies for running my notebook are pre-compiled there, just:

```
sudo apt-get install ipython3-notebook python3-graph-tool python3-joblib python3-scipy
```

You can also [view the example notebook in HTML].

[Jupyter]: http://jupyter.org/
[graph_tool]: https://graph-tool.skewed.de/
[view the example notebook in HTML]: https://rawgit.com/mcelrath/braidcoin/master/Braid%2BExamples.html


## TODO

fix bind mount problem:

- Docker for Mac ignores bind mount permissions?
- create blank etc/ipython and etc/jupyter folders?
- choose USER in Dockerfile, ./serve, or both?
- run Jupyter as root?

pip freeze to pin requirements?

README Docker cleanup, e.g. `docker rmi braidcoin`

books/Braid Examples:

- %pylab is deprecated, use %matplotlib inline
- Does python-bitcoinlib need `sudo apt-get install libssl-dev` ?

Update Dockerfile EXPOSE and CMD?

Use scipy.sparse instead of graph-tool? NetworkX for drawing?

Compare to DAG NIGHT: https://eprint.iacr.org/2022/1494.pdf
