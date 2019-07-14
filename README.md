<p align="center">
  <img width="300" height="300" src="https://user-images.githubusercontent.com/29679899/61179022-ffc9c900-a5c7-11e9-9be0-8b376a9b195b.png">
</p>


# Numerai LSTM

Numerai is an AI-run, crowd/open-sourced hedge fund/trading platform where competitors try to 
predict the movement of financial markets. 

I used an LSTM-RNN for regression analysis on Numerai's proprietary data and I used the same model to try and predict
the movement of Delphi Technologies and their split-off, Aptiv PLC. 

Delphi's <a href="http://blog.aylien.com/overview-word-embeddings-history-word2vec-cbow-glove" title="aylien.com" rel="nofollow">split-off</a></li> in December 2017 affected the company's original S & P 500 index. 
I recovered the data Delphi lost after the split and merged it into one dataset in an attempt to accurately predict the 
movement of their stocks based on the Opening and High price of the original index.

<p align="center">
  <br>
  <img src="https://user-images.githubusercontent.com/29679899/61179349-91d4d000-a5ce-11e9-9c13-7175909e69e3.png">
</p>

On the Delphi/Aptiv data, the model had a final loss of <b>1e-2</b> at <b>140</b> epochs:
<p align="center">
  <img src="https://media.giphy.com/media/ZBVQCX7KA2qSOwMLEf/giphy.gif">
</p>

But the model was capable of converging at <b>35</b> epochs with good results:

<p align="center">
  <br>
  <img src="https://media.giphy.com/media/dvlIA3HfG0abC3dtwN/giphy.gif">
</p>
