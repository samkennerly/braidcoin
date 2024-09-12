# Braidcoin

Experiments in a improving Bitcoin using a Directed Acyclic Graph


## run with Docker

If you have [Docker Desktop] installed, `cd` to this repo and run
```
./serve
```
then point a web browser here:
```
127.0.0.1:8888
```
The `serve` script creates a Docker image named `braidcoin:latest`, runs a container from that image, and starts a [Jupyter] server. Docker will [bind mount] folders from this repo and create `.ipython` and `.jupyter` folders if they do not exist. From inside the container, mounted folders appear in `/home/braidcoin/`.

Use Ctrl-C to stop the server. The container will delete itself. To delete the image, run
```
docker rmi braidcoin
```

[Docker Desktop]: https://www.docker.com/products/docker-desktop/
[Jupyter]: http://jupyter.org/
[bind mount]: https://docs.docker.com/engine/storage/bind-mounts/


## run without Docker

Running these examples requires [Jupyter] and the ipython kernel.  Fire up the example notebook in your browser by `jupyter notebook`.

We use [graph_tool] for plotting. This one is a bitch to compile, I recommend getting it from your friendly local pre-compiled distribution. I use Ubuntu 16.04.  The dependencies for running my notebook are pre-compiled there, just:

```
sudo apt-get install ipython3-notebook python3-graph-tool python3-joblib python3-scipy
```

You can also [view the example notebook in HTML].

[graph_tool]: https://graph-tool.skewed.de/
[view the example notebook in HTML]: https://rawgit.com/mcelrath/braidcoin/master/Braid%2BExamples.html


## TODO

books/Braid Examples:

- LaTeX errors: \lambda -> \\lambda, \prime -> \\prime
- %pylab is deprecated, use %matplotlib inline
- Does python-bitcoinlib need `sudo apt-get install libssl-dev` ?

figure out bind mount weirdness with Docker Engine for Linux

Use scipy.sparse instead of graph-tool? NetworkX for drawing?

Compare to DAG NIGHT: https://eprint.iacr.org/2022/1494.pdf
