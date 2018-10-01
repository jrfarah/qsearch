#!/usr/bin/env wolframscript
(* ::Package:: *)

(* ::Input::Initialization:: *)
(* functions to generate the shift and phase operators *)


(* ::Input::Initialization:: *)
Print["Program running!"]
\[Omega][d_]:= Exp[2 Pi I /d];
genX[d_]:=RotateLeft[IdentityMatrix[d]];
genZ[d_]:=DiagonalMatrix[Table[\[Omega][d]^n,{n,0,d-1}]];


(* ::Input::Initialization:: *)
(* generate a random vector and normalize it *)
genRandVec[d_]:=Normalize[RandomComplex[{-1-I,1+I},d]];


(* ::Input::Initialization:: *)
(* generate variables in greek and English alphabets to use as [[]] equivalents *)
genvec[number_]:=Normalize[#[[1]] E^(I #[[2]])&/@MapThread[List,{ToExpression[Take[Alphabet[],number]],ToExpression[Take[Alphabet["Greek"],number]]}]];


(* ::Input::Initialization:: *)
(* frame potential function *)


(* ::Input::Initialization:: *)
framePotential[vec_]:=Sum[Abs[Conjugate[vec].MatrixPower[genX[Length[vec]],k].MatrixPower[genZ[Length[vec]],l].vec]^4,{k,0,Length[vec]-1},{l,0,Length[vec]-1}];


(* ::Input::Initialization:: *)
(*The jk component of the quadruple product g matrix in terms of components of a WH fiducial vector*)
g[vec_,j_,k_]:=N[Sum[Conjugate[vec[[Mod[s,Length[vec]]+1]]] vec[[Mod[s+j,Length[vec]]+1]]vec[[Mod[s+k,Length[vec]]+1]]Conjugate[vec[[Mod[s+j+k,Length[vec]]+1]]],{s,0,Length[vec]-1}], 6];


(* ::Input::Initialization:: *)
genTable[d_, a_]:=Table[g[a,i,j],{i,0,d-1},{j,0,d-1}];


(* ::Input::Initialization:: *)
Print[$ScriptCommandLine]


(* ::Input::Initialization:: *)
Print[SetDirectory[Directory[]]]


(* ::Input::Initialization:: *)
a = genRandVec[ReadList["dim.dim", Number][[1]]]
(*a = genRandVec[#1]*)
Print[a]
ex[d_, a_]:=Export["table2.csv",genTable[d, a],"Table","LineSeparators"->", "];
ex[ReadList["dim.dim", Number][[1]], a]
