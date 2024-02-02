  from twtrr import shorten

  def main():
   tst_twtrr()


  def tst_twtrr():
    assert shorten('Aya')=="y"
    assert shorten('Hello')=="Hll"
    assert shorten('HIOKBUJG')=="HKBJG"
    assert shorten("jello")=="jll"
    assert shorten("HELLO")=="HLL"
    assert shorten("HELLO , jello")=="HLL , jll"
    assert shorten("CES23 , jello")=="CS23 , jll"
    assert shorten("CS23")=="CS23"

  if __name__ == "__main__":
    main()
