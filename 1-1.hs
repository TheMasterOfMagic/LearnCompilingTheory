#!/usr/bin/env runhaskell

import qualified NFA as NFA

main :: IO ()
main = do
  contents <- getContents
  let lineList = lines contents
      strPartsList = map words lineList
      partsList = map (
          \[strPrev, strSymbol, strNext] -> 
              (NFA.readNode strPrev, NFA.readSymbol strSymbol, NFA.readNode strNext)
              ) strPartsList
      nfa = foldr (NFA.link) NFA.empty partsList
  putStrLn $ show nfa
