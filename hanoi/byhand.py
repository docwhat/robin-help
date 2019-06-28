#!/usr/bin/pytTowerOfHanoion

TowerOfHanoi(5, "A", "C", "B")
    # n = 5
    # from_rod=A
    # to_rod=C
    # aux_rod=B
    5 != 0
    TowerOfHanoi(4, "A", "B", "C")
        # n = 4
        # from_rod=A
        # to_rod=B
        # aux_rod=C
        4 != 0
        TowerOfHanoi(3, "A", "C", "B")
            # n = 3
            # from_rod=A
            # to_rod=C
            # aux_rod=B
            3 != 0
            TowerOfHanoi(2, "A", "B", "C")
                # n = 2
                # from_rod=A
                # to_rod=B
                # aux_rod=C
                2 != 0
                TowerOfHanoi(1, "A", "C", "B")
                    # n = 1
                    # from_rod=A
                    # to_rod=C
                    # aux_rod=B
                    1 != 0
                    TowerOfHanoi(0, "A", "B", "C")
                        # n = 0
                        0 == 0
                        return
                    move(1, "A", "C")
                    TowerOfHanoi(0, )
                        # n = 0
                        0 == 0
                        return
                    return
                move(2, "A", "B")
                TowerOfHanoi(1, "C", "B", "A")
                    # n = 1
                    # from_rod=C
                    # to_rod=B
                    # aux_rod=A
                    1 != 0
                    TowerOfHanoi(0, "C", "A", "B")
                        # n = 0
                        0 == 0
                        return
                    move(1, "C", "B")
                    TowerOfHanoi(0, ...)
                        # n = 0
                        0 == 0
                        return
                    return
                return
            # n = 3
            # from_rod=A
            # to_rod=C
            # aux_rod=B
            move(3, "A", "C")
            TowerOfHanoi(2, "B", "C", "A")
