# UNIse - search engine
Search engine built over university material

## Install Notes
<ul>
	<li> The NLTK data is needed, specifically the <code>words, wordnet</code> and <code>omw</code> data are necessary </li>
	<li> To install NLTK data just open a <code>python</code> shell, <code>import nltk</code> and type <code>nltk.download("words")</code> for all the listed data </li>
	<li> Useful information can be found here https://www.nltk.org/data.html </li>
	<li> Everything else is handled by <code>pipenv</code> </li>
</ul>

## Setup
How to run:

```
$ cd UNIse
$ pipenv shell
$ pipenv install
$ flask run
```
Once the server start go to <i>localhost:5000</i> from the browser.

## Additional Info
<p> The search engine default index works with the directory <code>UNIse/unise/resources/test_data</code>. </p>
<p> This directory contains just a bunch of file, to create a new index just go to the <i>create</i> page from the homepage and follow the instructions. </p>
