# Othelo AI agent

*Search*

## MITRO
- Game-Theory (MinMax algorithm) MITRO206
- Depth search (branch and cut/branch and bound) MITRO205

## SD
- Adversarial ML
- RNN
- Prolog Symbolic (SD206)

## Custom solutions

Cut the board in small unities (with padding) and learn paterns based only on local areas to detect good moves. 
- Learn on 2x2 or 3x3 cells, give each configuration a score
- On a specific board setup, cut the board in cells and match them with the best winning cell configuration from learning
- Select then the best cell score and play
- Maybe : learn from it as well and update weights and scoring on cell moves

