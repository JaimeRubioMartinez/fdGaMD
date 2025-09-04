# Python subroutine to generate the optimized GaMD input files (size dependant)

def GEN_inputs_start_GaMD (system_name,num_atoms,dt,sigma0P,sigma0D,cut,fswitch) :

  ntave     =  4 * num_atoms
  ntcmdprep =  2 * ntave
  ntebprep  =  2 * ntave
  ntcmd     =  5 * ntave

  lmin      = 10000000
  lmax      = 50000000

  nteb_range = []
  NOT_select = True

  for index in range (1,51) :
    value = index * ntave
    nteb_range.append(value)

  for index in range (49,-1,-1) :
    nteb = nteb_range[index]
    if nteb <= lmax and nteb >= lmin :
      print ( ' ... Selected nteb =  {} * 4 * Num_Atoms = {} '.format(index+1,nteb ))
      NOT_select = False
      break

  if  NOT_select :
    if nteb_range[-1] <= lmax :
      nteb = nteb_range[-1]
    else :
      nteb = lmax
    print ( ' ... ... GaMD preparation -Forced : Selected nteb = {}'.format(nteb ) )

  gaMD_step1 = ntcmd + nteb
  name_ini   = system_name + '_099_dyn.in'
  send_fout  = open(name_ini,'w')
  send_fout.write(' First step preparing GaMD (c) NVT     '+ter)
  send_fout.write(' &cntrl                                '+ter)
  send_fout.write('  imin = 0, irest = 1, ntx = 5,        '+ter)
  send_fout.write('  ntc = 2, ntf = 2, dt = {},           '.format(dt)+ter)
  if use_fswitch :
    send_fout.write('  cut = {}, fswitch = {}, iwrap=1,   '.format(cut,fswitch)+ter)
  else : 
    send_fout.write('  cut = {}, iwrap=1,                 '.format(cut,fswitch)+ter)
  send_fout.write('  nstlim = {},                         '.format(gaMD_step1)+ter)
  send_fout.write('  ntb=1, ntp = 0,                      '+ter)
  send_fout.write('  ntpr   = 100000,                     '+ter)
  send_fout.write('  ntt = 3, gamma_ln = 3.0, ig = -1,    '+ter)
  send_fout.write('  temp0 = 300.0,                       '+ter)
  send_fout.write('  ntwv = 0, ntwe = 5000, ntwx = 5000,ntwr = 1000000,  '+ter)
  send_fout.write('  igamd = 3, iE = 1, irest_gamd = 0,                '+ter)
  send_fout.write('  ntcmdprep =  {}, ntcmd = {},   '.format(ntcmdprep,ntcmd)+ter)
  send_fout.write('  ntebprep  =  {}, nteb  = {},   '.format(ntebprep,nteb )+ter)
  send_fout.write('  ntave     =  {},               '.format(ntave)+ter)
  send_fout.write('  sigma0P =  {}, sigma0D = {},   '.format(sigma0P,sigma0D)+ter)
  send_fout.write(' &end    '+ter)
  send_fout.close()

  return

