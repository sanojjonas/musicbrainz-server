/*
 * @flow
 * Copyright (C) 2018 MetaBrainz Foundation
 *
 * This file is part of MusicBrainz, the open internet music database,
 * and is licensed under the GPL version 2, or (at your option) any
 * later version: http://www.gnu.org/licenses/gpl-2.0.txt
 */

const React = require('react');

const SubHeader = ({subHeading}: {subHeading: string}) => (
  <p className="subheader">
    <span className="prefix">{'~'}</span>{' '}{subHeading}
  </p>
);

module.exports = SubHeader;