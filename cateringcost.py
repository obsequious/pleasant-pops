pops = raw_input("How many pops? ")
time = raw_input("And how much time? ")

pops = float(pops)
time = float(time)

pop_cost = pops * 2.50
time_cost = time * 75.0
dc_sales_tax = pop_cost * .1

print "Pop cost (out of state): %.2f" % pop_cost
print "Pop cost (DC): %.2f" % (pop_cost + dc_sales_tax)
print "Time cost: %.2f" % time_cost
print "Total cost (out of state): %.2f" % (pop_cost + time_cost)
print "Total cost (DC): %.2f" % (pop_cost + time_cost + dc_sales_tax)