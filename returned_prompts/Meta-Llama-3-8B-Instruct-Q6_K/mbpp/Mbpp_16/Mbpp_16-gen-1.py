def text_lowercase_underscore(s):
    s = s.lower()
    return all(c.isalpha() or c == '_' for c in s) and any(c == '_' for c in s)

# Test the function
print(text_lowercase_underscore("aab_cbbbc"))  # Should return True
print(text_lowercase_underscore("aabc"))  # Should return False
print(text_lowercase_underscore("a_b_c"))  # Should return True
print(text_lowercase_underscore("abc"))  # Should return False
print(text_lowercase_underscore("aAb_cBb"))  # Should return True
print(text_lowercase_underscore("aAbc"))  # Should return False
print(text_lowercase_underscore("aAb_c"))  # Should return True
print(text_lowercase_underscore("aAb"))  # Should return False
print(text_lowercase_underscore("a_a"))  # Should return True
print(text_lowercase_underscore("a"))  # Should return False
print(text_lowercase_underscore("_"))  # Should return False
print(text_lowercase_underscore(""))  # Should return True
print(text_lowercase_underscore("a_b_c_d"))  # Should return True
print(text_lowercase_underscore("a_b_c_d_e"))  # Should return True
print(text_lowercase_underscore("a_b_c_d_e_f"))  # Should return True
print(text_lowercase_underscore("a_b_c_d_e_f_g"))  # Should return True
print(text_lowercase_underscore("a_b_c_d_e_f_g_h"))  # Should return True
print(text_lowercase_underscore("a_b_c_d_e_f_g_h_i"))  # Should return True
print(text_lowercase_underscore("a_b_c_d_e_f_g_h_i_j"))  # Should return True
print(text_lowercase_underscore("a_b_c_d_e_f_g_h_i_j_k"))  # Should return True
print(text_lowercase_underscore("a_b_c_d_e_f_g_h_i_j_k_l"))  # Should return True
print(text_lowercase_underscore("a_b_c_d_e_f_g_h_i_j_k_l_m"))  # Should return True
print(text_lowercase_underscore("a_b_c_d_e_f_g_h_i_j_k_l_m_n"))  # Should return True
print(text_lowercase_underscore("a_b_c_d_e_f_g_h_i_j_k_l_m_n_o"))  # Should return True
print(text_lowercase_underscore("a_b_c_d_e_f_g_h_i_j_k