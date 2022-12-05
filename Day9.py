import time

a = """22
16
24
45
43
46
28
38
27
49
42
12
48
8
6
13
26
39
18
9
1
33
7
34
15
10
21
14
17
11
16
19
59
31
24
27
35
28
20
46
36
45
8
76
12
50
18
22
23
37
33
25
47
26
32
43
30
34
38
31
39
40
35
28
20
41
36
42
45
57
48
44
46
76
51
55
53
50
52
87
56
75
54
66
59
60
61
62
131
64
90
78
88
116
92
94
95
145
150
101
105
197
250
146
110
123
113
224
121
140
229
125
126
142
152
195
166
180
186
207
189
196
211
325
206
228
223
478
231
233
371
359
246
369
292
251
267
745
294
513
346
375
385
382
488
395
402
417
615
439
451
454
464
626
728
540
543
497
518
653
545
561
669
640
785
721
757
767
777
797
812
819
856
890
893
905
1390
1040
1037
1061
1085
1015
1274
1285
1795
1496
1358
1533
1736
1506
2209
1544
2164
1574
3269
1631
1675
1945
1783
2325
2055
2868
2614
3002
2076
2760
3610
2559
2643
2854
3029
3164
3077
5723
4426
3118
3175
3205
3249
3306
3414
3458
4021
3838
4131
5173
5672
4635
4719
4836
5202
5807
5413
6103
7327
11458
6241
6195
6293
9145
6367
10914
9223
6555
6720
13134
12227
7859
7969
9938
13087
9354
11009
9555
14190
10615
11220
17155
12298
18978
12436
14100
12750
12660
18773
12922
13275
14689
24627
18474
15828
17213
28328
19969
18909
20170
20363
20564
20775
29089
32983
25582
24734
25048
25096
25186
25410
25672
25935
26197
27964
30517
39423
33041
39079
34737
36122
40744
50880
48739
50458
41138
41339
77828
49782
55565
49830
49920
50234
51293
50858
55927
52132
67778
54161
58481
101751
69163
118236
70859
76076
76866
81882
82477
89877
108311
90920
92632
102990
99750
181632
126310
145081
112642
208192
105019
106293
110613
121939
130237
127644
191628
172153
399820
186901
152942
158748
164359
344570
254236
183552
190670
192382
265041
249583
216906
211312
263555
338956
215632
226958
232552
311196
252176
257881
506412
339843
400458
474787
717724
375654
627416
521436
463488
374222
401982
460895
403694
779317
426944
449458
438270
733370
442590
758588
479134
484728
805676
779348
1102203
714065
715497
776112
802598
749876
841964
776204
835117
823680
844572
851440
830638
846284
906078
1248266
880860
917404
1983063
1578802
1561186
1584993
1656972
1537745
1741084
1429562
1463941
1465373
2308513
1644562
1526080
2090230
2296011
1669964
1654318
1675210
1676922
2525422
1763688
1786938
3298880
2381345
2955642
4471575
3314526
2893503
2929314
3003118
2894935
2990021
2991453
3108503
3109935
3170642
3180398
3324282
6136040
5849704
7811250
4200632
3352132
6494924
3550626
4145033
5384463
5489848
6305979
5788438
5822817
6183516
5824249
5884956
5993139
6540647
6098524
6315735
10384148
6504680
6731024
7325431
11625888
6902758
9690480
11361876
7497165
7695659
8935089
9040474
9529496
11172901
11278286
11611255
11647066
11707773
17187645
11709205
11878095
17286906
18193830
15021090
12820415
13235704
13407438
16432254
14228189
14399923
17026661
18730954
15192824
16736133
28673727
17975563
14360655
24408605
22451187
26804079
34160392
32959143
23416978
23587300
24529620
38808528
29381745
26056119
36851110
26227853
26643142
29553479
31096788
28588844
31928957
31387316
56357558
33168387
32336218
36811842
37777633
58142323
45868165
51333699
47004278
47946598
48116920
49473097
72511307
50585739
54816697
52283972
73232131
55231986
52870995
78933235
59976160
63316273
68740799
63723534
102236264
78204383
84620190
69148060
82680007
132464333
131804230
111670132
100817593
94950876
130488355
97590017
100058836
102869711
175794400
118540231
105154967
168878501
108102981
123292433
123699694
210668716
195120503
200876429
132871594
147352443
151828067
153768250
233358066
205692998
200105843
259931048
192540893
195009712
197648853
200459728
202744984
256983034
208024678
213257948
223695198
356513234
275120500
231395414
411759115
271052137
280224037
284699661
286639844
338564592
460390776
429388196
387550605
405798841
431719876
400565571
413717676
390189746
494747335
398108581
403204712
410769662
421282626
436953146
444653362
455090612
741769304
557691981
671617708
709612233
1204359568
989836270
571339505
625204436
793394458
801313293
819577942
777740351
788298327
790755317
1152538966
800959408
808878243
813974374
1413387012
858295324
832052288
1116271070
1008292651
1299461285
1012782593
1129031486
1182896417
1334816669
1385313879
1196543941
1359637832
1589611620
1799047968
1602272701
1566038678
1646026662
1578699759
1579053644
1591714725
1609837651
1614933782
1622852617
3212464237
1690347612
2014948705
1844834881
2129053663
2137324137
2141814079
3729038862
2311927903
2581857820
3201552376
2556181773
2762582619
2925676510
3144738437
3145092322
3459768663
3157753403
3188891295
3193633541
3237786399
3206648507
4204710437
3305281394
3827671749
3535182493
3982159018
3859783586
4270867742
5286906401
5819644219
5726596257
4893785723
4868109676
6724073788
6083429913
5318764392
5688259129
9961860187
6302845725
6333983617
6346644698
6444434906
9491616838
6400282048
6511929901
10494088919
6840463887
7132953143
7362854242
8822088894
13182498461
8130651328
9761895399
10155016077
14385402561
10186874068
10212550115
11007023521
16295843804
13577388049
11621610117
11991104854
12636829342
12791079604
12680628315
15662552781
12956364807
16273825300
13240745935
13352393788
16995479964
13973417030
22174482682
15493505570
25593194149
17892546727
33386052297
23003629719
26450859881
20399424183
21193897589
49454489600
24584411570
24258439459
26143473392
24671733169
25231850789
25636993122
25471707919
53785476480
26197110742
26308758595
26593139723
33751817971
38557828600
38291970910
34372841213
37667988252
57376470932
39086444316
45071157352
41593321772
43403053902
44657863642
45452337048
65395202911
48842851029
59604692002
51945751717
49903583958
50143441088
50703558708
51108701041
52790250465
52505869337
60569951955
84860519012
72930669813
68124659184
88435411998
94383572237
85481542254
76754432568
83744307958
125597283597
130552699606
99951552070
88060917544
93500714671
94295188077
127863133609
100607142666
100047025046
253460417206
194990714903
100846999796
103493809173
103614570378
197909758455
180369002946
172977694859
180248241741
141055328997
144879091752
160498740526
188975351427
176801457614
164815350112
171805225502
244830643822
181561632215
188107942590
441568359796
187795902748
204221713044
352923292702
368476945536
276471504032
204340808969
572698658580
426392276037
244669899375
380086074410
332303966028
326440723967
312860554499
285934420749
301554069523
305377832278
325314090638
336620575614
432626546570
346376982327
353366857717
369357534963
369669574805
375903845338
392017615792
392136711717
480693217076
622554996363
449010708344
480812313001
490275229718
530604320124
655603995554
654920927240
655291955712
591312253027
696110298772
913319763646
587488490272
606931901801
630691922916
924109065886
682997557941
699743840044
716046557132
1176922611773
899961855087
767921461130
1047309571504
784154327509
882411941435
929703925420
929823021345
939285938062
1020879549842
1077763719990
1118092810396
1947271426591
1178800743299
1274309810968
1218180413188
1270486048213
1194420392073
1287232330316
1616008412219
1483898167553
1892969168905
1382741397985
1817836650440
1684116182596
1552075788639
1650333402565
1666566268944
1713858252929
1713977348854
1821697879497
3499347215230
1869108959407
1960165487904
2239059963030
2195856530386
2412600805261
4305569974166
2396981156487
2464906440286
3316899671509
2481652722389
3531813999294
3033074800550
2866639565538
2934817186624
3049307666929
3204439277482
3202409191204
3218642057583
7524212031749
5263620722025
4064965489793
4735748524945
3535675228351
4060757842527
5615009996465
3829274447311
5601420433969
5443499240512
4677509252775
4809581961748
4861887596773
4878633878876
4946559162675
5348292287927
5915947232467
7361088446605
5801456752162
7114273156722
5984124853553
6251716858133
6738084419555
6421051248787
8926853086566
7600640718144
8874547451541
8691162044084
10121008493287
8414309107227
10080991305444
8506783700086
8638856409059
9487091214523
16475188169685
9539396849548
9688215840624
14835383502450
17381331151627
15489672592786
12053173610295
11717403984629
11785581605715
12222508000949
18831677141351
20927721061836
15939932698757
13159135668342
20224187684715
16014949825371
16107424418230
16921092807313
17197945744170
27657336683386
25628148539381
17145640109145
18125947623582
18178253258607
19227612690172
27717650108155
28519892981975
21473797446339
23502985590344
23770577594924
23838755216010
23939911985578
49131134129725
37145280492028
28237457826320
29099068367099
34119038551483
38671743190509
36662121258686
32122374243601
32936042632684
38619437555484
34066732916458
34343585853315
42118165244185
35271587732727
35323893367752
52244986175065
55892951838525
76184898160643
60145540636848
44976783036683
45413709431917
59162648583762
47609332810934
79757295285232
52177369811898
57336526193419
60359832069921
69615173586042
67446267611353
65058416876285
68207630365411
66189107160059"""

b = list(map(int, a.splitlines()))


def task17():
    for i in range(len(b)):
        m = False
        for j in range(25):
            for l in range(25):
                if int(b[i+25]) == int(b[i+j]) + int(b[i+l]):
                    m = True
        if not m:
            return b[i+25]


def task18():
    l = task17()
    for i in range(len(b)):
        for j in range(len(b)-i):
            if sum(b[i:j]) == l:
                return max(b[i:j]) + min(b[i:j])


t1 = time.time()
print(task18())
t2 = time.time()
print(t2-t1)