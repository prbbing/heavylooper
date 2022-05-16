from ROOT import *

out = TFile('out.root', "RECREATE")
hist = TH2F("rvsq", "rvsq", 300,0,300,100,0,10)

for i in range(0,300):
  for j in range(0,100):
    r = (i+0.00001)/1000.0
    q = 0.1*j + 0.00001
    pT = 0.6*r*q
    hist.Fill(r*1000, q, pT) 

out.cd()
hist.Write()
out.Close()
