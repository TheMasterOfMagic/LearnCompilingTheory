module NFA where

import qualified Data.List as List
import qualified Data.Map as Map
import qualified Data.Set as Set
import qualified Data.Maybe as Maybe

type Node = Int
showNode :: Node -> String
showNode node = show node
readNode :: String -> Node
readNode string = read string::Node

type NodeSet = Set.Set Node
showNodeSet :: NodeSet -> String
showNodeSet nodeSet = "[" ++ (concat $ List.intersperse "," $ map showNode $ Set.toList nodeSet) ++ "]"

type Symbol = Char
showSymbol :: Symbol -> String
showSymbol symbol = [symbol]
readSymbol :: String -> Symbol
readSymbol [symbol] = symbol

type OutEdges = Map.Map Symbol NodeSet
showOutEdges :: OutEdges -> String
showOutEdges outEdges = "[" ++ (concat $ List.intersperse "," $ map (\(symbol, nodeSet) -> ("(" ++ showSymbol symbol ++ "," ++ showNodeSet nodeSet ++ ")")) $ Map.toList outEdges) ++ "]"

type NFATable = Map.Map Node OutEdges
showNFATable :: NFATable -> String
showNFATable nfaTable = "[" ++ (concat $ List.intersperse "," $ map (\(node, outEdges) -> ("(" ++ showNode node ++ "," ++ showOutEdges outEdges ++ ")")) $ Map.toList nfaTable) ++ "]" 

data NFA = NFA NFATable
instance Show NFA where
    show (NFA nfaTable) = showNFATable nfaTable

empty :: NFA
empty = NFA Map.empty

link :: (Node, Symbol, Node) -> NFA -> NFA
link (prev, symbol, next) (NFA nfaTable) = NFA nfaTable'
    where
        outEdges = Maybe.fromMaybe Map.empty $ Map.lookup prev nfaTable
        nodeSet = Maybe.fromMaybe Set.empty $ Map.lookup symbol outEdges
        nodeSet' = Set.insert next nodeSet
        outEdges' = Map.insert symbol nodeSet' outEdges
        nfaTable' = Map.insert prev outEdges' nfaTable