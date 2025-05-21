from trism import TritonModel
import numpy as np

model = TritonModel(
    model="mbert.qry",
    version=1,
    url="localhost:8011",
    grpc=True
)

for inp in model.inputs:
  print(f"📥 Inputs name: {inp.name}, Inputs shape: {inp.shape}, Inputs datatype: {inp.dtype}\n")

for out in model.outputs:
  print(f"📤 Outputs name: {out.name}, Outputs shape: {out.shape}, Outputs datatype: {out.dtype}\n")