import django
import torch
import torch.nn as torch_nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

from services import test_suite
from tradeModels import MLModel as model
from tradeModels.ml import StockDataset

django.setup()
from tradeEngine.models import TestTrade

LEARNING_RATE = 0.05
EPOCHS = 200

loss_function = model.loss_function
# optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

def main():
  test_suite.generate()
  test_suite.validate()
  # t = TestTrade.objects.get(pk=1)
  # print('t', t)
  input_dimension = 7
  output_dimension = 4
  # should hidden size be the same as the input dimension?
  hidden_dimension = 12
  batch_size = 20
  # do we really need mulitple layers?
  layers = 2
  # StockMLModel = model()
  # optimizer = model.optimizer
  # lets use GRU over LSTM
  lstm = torch_nn.GRU(input_dimension, hidden_dimension, 2)
  # seq_len, batch, input_size
  _input = torch.randn(batch_size, 1, input_dimension)
  linear = torch_nn.Linear(hidden_dimension, output_dimension)
  print('input', _input.size())

  out, (h, c) = lstm(_input)
  print('lstm out size', out.size())
  # print(h.size())
  # print(c.size())
  # out_linear = linear(out.view(batch_size, output_dimension))
  t = torch.Tensor([[1,2,3], [4,5,6]])
  # print('t', t)
  # print('t', t[-1,:])
  # print(out[-1, :, :].size())
  out_linear = linear(out[-1, :, :])
  # print('out linear size', out_linear.size())
  # for _ in range(EPOCHS):
  #   pass
  # train that bad boy
  stocks = StockDataset(csv_file='data/model_data.csv')
  # print('0th', stocks[0])

  # for i in range(len(stocks)):
  #   print(stocks[i])

  dataloader = DataLoader(
    stocks,
    batch_size=1,
    shuffle=True,
    num_workers=0,
    drop_last=True
  )
  print('len of dataloader', len(dataloader))

  for i, batch in enumerate(dataloader):
    print('i', i)
    # print('batch', batch)





if __name__ == '__main__':
  main()
