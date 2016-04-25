RM=rm -f
DESTDIR=$(SR_CODE_BASE)/snaproute/src/out/bin
MKDIR=mkdir -p
RSYNC=rsync -rupE

COMP_NAME=sdk
SRCS=flexswitchV2.py\
	  flexprint.py\

all: install 
clean:;
install:
	@$(MKDIR) $(DESTDIR)/sdk/py/
	install $(SRCS) $(DESTDIR)/sdk/py/

guard:
ifndef SR_CODE_BASE
	 $(error SR_CODE_BASE is not set)
endif

clean:guard
	 $(RM) $(DESTDIR)/$(COMP_NAME) 
