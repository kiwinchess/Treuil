
   RDM - Ossatures
   Calcul des Structures par la M�thode des �l�ments Finis

   Version  - 6.17 - 29 mars 2011

   Utilisateur : ensta

$debut du fichier
$version
6.17
$SI unites
$nom du fichier
vertical.por
$date
19/6/2019
$heure
16/43/24
$ossature
spatiale
$noeuds ( 6 )
   1  0.00000000000E+00  0.00000000000E+00  1.28000000000E+00
   2  0.00000000000E+00  8.00000000000E-01  1.28000000000E+00
   3  0.00000000000E+00  8.00000000000E-01  0.00000000000E+00
   4  0.00000000000E+00  1.65000000000E+00  1.28000000000E+00
   5  0.00000000000E+00  0.00000000000E+00  0.00000000000E+00
   6  0.00000000000E+00  8.00000000000E-01  1.78000000000E+00
   0
$poutres ( 7 )
   1 RIRI     1    2  1.00000000000E+00 -0.00000000000E+00  0.00000000000E+00 11 11
   2 RIRI     3    2  0.00000000000E+00 -1.00000000000E+00  0.00000000000E+00 11 11
   3 RIRI     2    4  1.00000000000E+00 -0.00000000000E+00  0.00000000000E+00 11 11
   4 RIRI     5    1  0.00000000000E+00 -1.00000000000E+00  0.00000000000E+00 11 11
   5 RIRI     2    6  0.00000000000E+00 -1.00000000000E+00  0.00000000000E+00 11 11
   6 RIRI     6    4  1.00000000000E+00 -0.00000000000E+00  0.00000000000E+00 11 11
   7 RIRI     6    1 -1.00000000000E+00 -0.00000000000E+00  0.00000000000E+00 11 11
   0
$sections
11
TYPE BIBLIOTHEQUE
NOM *Rond creux
DESIGNATION *d=60.3 e=5.0
LOGO 2
DIMENSIONS 2
 6.030000E-02
 5.000000E-03
AIRE  8.68650368718E-04
IYY  3.34765908161E-07
IZZ  3.34765908161E-07
WPY  1.53319870000E-05
WPZ  1.53319880000E-05
TORSION  6.69531820000E-07
KYY  0.5067900
KZZ  0.5067900
///
0
$materiaux
11
NOM Acier Inox
MOD  2.030E+11
POI 0.2900
MAS 7850.00
DIL  1.5000E-05
LIM  2.000E+08
///
0
$liaisons ( 2 )
encastrement 5
encastrement 3
///
$gpesanteur
10.000
$cas de charges
1
nom poids
poids    0
fnod    4  0.00000000000E+00  0.00000000000E+00 -2.65000000000E+03
////
$modes propres
nombre 1
methode sous_espace
precision 1.00000E-02
decalage_spectral 0.00000E+00
////
$maillage
20
$fin du fichier
