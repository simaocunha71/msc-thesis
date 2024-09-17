from nose.tools import assert_equal
def div_list(l1,l2):
    div_list = []
    for i in range(len(l1)):
        div_list.append(l1[i]/l2[i])
    return div_list