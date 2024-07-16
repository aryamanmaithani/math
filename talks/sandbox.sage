def tex(G):
	V = G.vertices(sort=True)
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	new_names = {V[i] : "$" + alphabet[i] + "$" for i in range(len(V))}
	G.relabel(new_names)
	G.latex_options().set_options(scale=0.6)

	return latex(G)