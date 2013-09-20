Title: Demystifying Data Centric Consistency Models - Part 1
Date: 2013-05-15 09:00
Tags: distributed, datastores
Category: Distributed Computing
Slug: demystifying-data-centric-consistency-models-part-1
Author: Zakiullah Khan Mohammed
status: draft
Summary: Consistency & Replication strategies are crucial aspect of distributed datastores. In a two a part blog post series, introduction to data centric consistency models would be done. This part would cover what consistency model means, classification and deal with explicit synchronization models in particular.

Before we move further, I think its better to understand certain terminology which is common to any distributedd system.

- **Availablity**: portion of time for which a service would be accessible.

- **Faul Tolerance**: guarantees strictly correct behaviour despite a certain type and number of faults.

- **Replication**: storing multiple physical copies of a single logical data item (object).

- **Concurrency**: its a property of system in which several computations are executing simultaneaously and potentially interacting with each other.

Consistency model is basically defined as a contract between a (distributed) data store and processes, in which the data store specifices what the result of the read and write operations are in the presence of concurrency. Consistency models can be further divided into data-centric and client-centric. This post focusses only on data-centric models, and in coming time I would write about client-centric models too.

Data centric Consistency models can be further divided into models where there are no explicity synchronization operations and models where there are explicit synchronization operations. This post would cover various types of data-centric consistency models where there are no explicit synchronization operations. And the next coming post would cover the later types.

When dealing with systems which adhere to no explicit synchronization operations, different types of consistency models prevail, namely:

- **Strict**: absolute time ordering of all shared accesses matters.

- **Lienarizability**: all processes must see all shared accesses in the same oreder. Accessess are furthermore ordered according to a (non-unique) global timestamp.

- **Sequential**: all process see all shared accessess in the same order. Accesses are not ordered in time.

- **Casual**: all processes see casually-realted shared accessess in same order.

- **FIFO**: all processes see writes from each other in the order they were used. Writes from different processes man not always be seen in that order.
