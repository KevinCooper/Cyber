
import angr
proj = angr.Project('./col')
#20 Character input plus newline
argv1 = angr.claripy.BVS("argv1", 20*8)

initial_state = proj.factory.entry_state(args=["./col", argv1])
#Number of bits to chop the bitvec into, each byte is 8 bits
for b in argv1.chop(8):
    initial_state.add_constraints( b >= 0x21 )
    initial_state.add_constraints( b <= 0x7e )
    #initial_state.add_constraints( b != 0 )

#create a path group using the created initial state 
pg = proj.factory.path_group(initial_state)

#Use to debug stuff
angr.path_group.l.setLevel("DEBUG")

#symbolically execute the program until we reach the wanted value of the instruction pointer
pg.explore(find=0x8048592)

found = pg.found[0]
    
#ask to the symbolic solver to get the value of argv1 in the reached state
solution = found.state.se.any_str(argv1)

print repr(solution)
