##
#	Inboxen.org specific tasks
##

.PHONY: setup-node
setup-node:
	nodeenv -p -n 8.16.0 --with-npm

.PHONY: install-watermelon-py-deps
install-watermelon-py-deps:
	echo "Warning: this command is very specific to inboxen.org. It will be removed in the near future."
	pip-sync extra/requirements/watermelon.inboxen.org.txt || pip install -r extra/requirements/watermelon.inboxen.org.txt

.PHONY: install-watermelon-deps
install-watermelon-deps: install-watermelon-py-deps install-js-deps
	echo "Warning: this command is very specific to inboxen.org. It will be removed in the near future."

# common deployment stuff
.PHONY: common-deploy
common-deploy:
	$(MAKE) install-watermelon-deps
	mkdir -p logs run
	$(MAKE) static
	./manage.py migrate
	./manage.py check --deploy
	touch inboxen/wsgi.py
	$(MAKE) celery-start salmon-start

.PHONY: deploy-%
deploy-%:
	echo "Warning: this command is very specific to inboxen.org. It will be removed in the near future."
	git fetch --prune
	git verify-tag $@
	-$(MAKE) celery-stop salmon-stop
	git checkout $@
	$(MAKE) common-deploy

.PHONY: dev-deploy
dev-deploy:
	echo "Warning: this command is very specific to inboxen.org. It will be removed in the near future."
	-$(MAKE) celery-stop salmon-stop
	git describe --dirty
	$(MAKE) common-deploy
